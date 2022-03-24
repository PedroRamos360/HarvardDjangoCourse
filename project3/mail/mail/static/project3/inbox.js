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

function compose_email() {
	// Show compose view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';
	document.querySelector('#email-view').style.display = 'none';

	// Clear out composition fields
	document.querySelector('#compose-recipients').value = '';
	document.querySelector('#compose-subject').value = '';
	document.querySelector('#compose-body').value = '';
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
		var new_email = document.createElement('div');
		new_email.className = 'email';
		new_email.id = email.id;
		var sender = document.createElement('strong');
		sender.appendChild(document.createTextNode(email.sender));
		sender.id=email.id;
		var subject = document.createElement('p');
		subject.className='fit'
		subject.id=email.id;
		subject.appendChild(document.createTextNode(email.subject));
		var timestamp = document.createElement('p');
		timestamp.className='fit';
		timestamp.id=email.id;
		timestamp.appendChild(document.createTextNode(email.timestamp));
		new_email.appendChild(sender);
		new_email.appendChild(subject);
		new_email.appendChild(timestamp);
		emails.appendChild(new_email);
	})
	emails_div.innerHTML = emails.innerHTML;
	localStorage.setItem('last_page', mailbox);
	document.querySelector('.email').addEventListener('click', event => load_email(event));
}

function load_email(event) {
	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-view').style.display = 'flex';

	console.log(event.target.id);
	fetch(`emails/${event.target.id}`)
	.then(response => response.json())
	.then(result => {
		console.log(result);
	})

	var email_div = document.querySelector('#email-view');
	var content_div = document.createElement('div');
	var from = document.createElement('strong');
	from.appendChild(document.createTextNode('From'));
	var to = document.createElement('strong');
	to.appendChild(document.createTextNode('To'));
	var subject = document.createElement('strong');
	subject.appendChild(document.createTextNode('Subject'));
	var timestamp = document.createElement('strong');
	timestamp.appendChild(document.createTextNode('Timestamp'));
	content_div.appendChild(from);
	content_div.appendChild(to);
	content_div.appendChild(subject);
	content_div.appendChild(timestamp);
	email_div.innerHTML = content_div.innerHTML;
}