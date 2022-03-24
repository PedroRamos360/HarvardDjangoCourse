document.addEventListener('DOMContentLoaded', function() {
	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', compose_email);
	document.querySelector('#compose-form').addEventListener('submit', submit_form);

	if (localStorage.getItem('last_page')) {
		var last_page = localStorage.getItem('last_page');
		if (last_page === 'compose_email') {
			compose_email();
		}
		else {
			load_mailbox(last_page);
		}
	} else {
		load_mailbox('inbox');
	}
});

function createElement(element, text=null, id=null, className=null, style=null) {
	var new_text = document.createElement(element);
	if (text)
		new_text.appendChild(document.createTextNode(text));
	if (id)	
		new_text.id = id;
	if (className)
		new_text.className=className;
	if (style)
		new_text.style = style;
	return new_text;
}

function compose_email(data=null) {
	// Show compose view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';
	document.querySelector('#email-view').style.display = 'none';

	if (data && data.id) {
		document.querySelector('#compose-recipients').value = data.sender;
		document.querySelector('#compose-subject').value = data.subject;
		document.querySelector('#compose-body').value = `On ${data.timestamp} ${data.sender} wrote: ${data.body}`;
	} else {
		document.querySelector('#compose-recipients').value = '';
		document.querySelector('#compose-subject').value = '';
		document.querySelector('#compose-body').value = '';
	}
	
	localStorage.setItem('last_page', 'compose_email');
}

function submit_form() {
	var recipients = document.querySelector('#compose-recipients').value;
	var subject = document.querySelector('#compose-subject').value;
	var content = document.querySelector('#compose-body').value;
	fetch('/emails', {
		method: 'POST',
		body: JSON.stringify({
			recipients: recipients,
			subject: subject,
			body: content
		})
	}).then(response => response.json())
	.then(result => {
		console.log(result);
		load_mailbox('sent');
	});
}

async function load_mailbox(mailbox) {
	var now_mailbox;
	await fetch(`/emails/${mailbox}`)
	.then(response => response.json())
	.then(result => {
		now_mailbox = result;
	});

	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'block';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-view').style.display = 'none';

	// Show the mailbox name
	document.querySelector('#title').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
	var emails_div = document.querySelector('#emails');
	var emails = document.createElement('div');
	now_mailbox.forEach(email => {
		if (email.read)
			var new_email = createElement('div', null, email.id, 'email read');
		else
			var new_email = createElement('div', null, email.id, 'email');
		var sender = createElement('strong', email.sender, email.id, 'fit');
		var subject = createElement('p', email.subject, email.id, 'fit');
		var timestamp = createElement('p', email.timestamp, email.id, 'fit');
		new_email.appendChild(sender);
		new_email.appendChild(subject);
		new_email.appendChild(timestamp);
		emails.appendChild(new_email);
	})
	emails_div.innerHTML = emails.innerHTML;
	localStorage.setItem('last_page', mailbox);
	var emails = document.querySelectorAll('.email');
	emails.forEach(email => {
		email.addEventListener('click', event => load_email(event));
	})
}

async function change_archive(email_id, boolean) {
	await fetch(`/emails/${email_id}`, {
		method: 'PUT',
		body: JSON.stringify({
			archived: boolean
		})
	});
	if (boolean)
		load_mailbox('inbox');
	else
		load_mailbox('archive');
}

async function load_email(event) {
	var user_logged = JSON.parse(document.getElementById('user_logged').textContent);
	var data;

	await fetch(`emails/${event.target.id}`)
	.then(response => response.json())
	.then(result => {
		data = result;
	});

	await fetch(`/emails/${data.id}`, {
		method: 'PUT',
		body: JSON.stringify({
			read: true
		})
	});

	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-view').style.display = 'flex';
	
	

	var email_div = document.querySelector('#email-view');
	var content_div = document.createElement('div');
	var i = 0;
	new_data = [data.sender, data.recipients, data.subject, data.timestamp];
	['From:', 'To:', 'Subject:', 'Timestamp:'].forEach(text => {
		var container_div = createElement('div', null, null, 'container_div');
		var new_strong = createElement('strong', text);
		var new_p = createElement('p', new_data[i], null, 'fit');
		new_p.style='margin-left:10px;'
		container_div.appendChild(new_strong);
		container_div.appendChild(new_p);
		content_div.appendChild(container_div);
		i++;
	});
	var buttons_div = createElement('div', null, null, null, 'display:flex;')
	if (user_logged != data.sender)
		buttons_div.appendChild(content_div.appendChild(createElement('button', 'Reply', 'reply', 'btn btn-sm btn-outline-primary', 'width:100px;margin-right:10px;')));
	if (localStorage.getItem('last_page') === 'archive') {
		buttons_div.appendChild(content_div.appendChild(createElement('button', 'Unarchive', 'unarchive', 'btn btn-sm btn-outline-primary', 'width:100px;')));
	}
	else {
		buttons_div.appendChild(content_div.appendChild(createElement('button', 'Archive', 'archive', 'btn btn-sm btn-outline-primary', 'width:100px;')));
	}


	content_div.appendChild(buttons_div);
	content_div.appendChild(createElement('hr', null, null, null, 'width:100%;'));
	content_div.appendChild(createElement('p', data.body));
	email_div.innerHTML = content_div.innerHTML;
	document.querySelector('#reply').addEventListener('click', () => {compose_email(data)});
	if (localStorage.getItem('last_page') === 'archive')
		document.querySelector('#unarchive').addEventListener('click', () => {change_archive(data.id, false)});
	else
		document.querySelector('#archive').addEventListener('click', () => {change_archive(data.id, true)});
}