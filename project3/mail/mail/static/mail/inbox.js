document.addEventListener('DOMContentLoaded', function() {
	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', compose_email);
	document.querySelector('#compose-form').addEventListener('submit', submit_form);

	if (localStorage.getItem('last_page')) {
		var last_page = localStorage.getItem('last_page');
		if (last_page === 'compose_email')
			compose_email();
		else
			load_mailbox(last_page);
	} else {
		load_mailbox('inbox');
	}
});

function compose_email() {
	// Show compose view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';

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

function load_mailbox(mailbox) {
	var banana = "{{banana}}";
	console.log(banana);
	var sent = '{{ sent|escapejs }}';
	var archived = '{{ archived|escapejs }}';

	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'block';
	document.querySelector('#compose-view').style.display = 'none';

	// Show the mailbox name
	document.querySelector('#title').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
	var emails_div = document.querySelector('#emails');
	inbox.forEach(email => {
		var new_email = document.createElement('div');
		new_email.className = 'email';
		emails_div.appendChild(new_email);
	})
	localStorage.setItem('last_page', mailbox);
}