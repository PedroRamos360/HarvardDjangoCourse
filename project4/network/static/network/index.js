async function changeHeart(event) {
    var heart = event.target;
    var post_id = event.target.parentElement.id;
    var counter = document.querySelector(`#p${post_id}`)
    if (heart.id === 'heart-liked') {
        heart.style.color = 'white';
        heart.id = 'heart';
        counter.innerHTML = parseInt(counter.innerHTML) - 1;
        await fetch('/like', {
            method: 'POST',
            body: JSON.stringify({
                post_id: event.target.parentElement.id,
                like: false
            })
        })
    }
    else {
        heart.style.color = 'red';
        heart.id = 'heart-liked';
        counter.innerHTML = parseInt(counter.innerHTML) + 1;
        await fetch('/like', {
            method: 'POST',
            body: JSON.stringify({
                post_id: event.target.parentElement.id,
                like: true
            })
        })
    }
}

async function handleSave(post_id, event) {
    textarea = document.querySelector(`#t${post_id}`);
    body = textarea.value;
    await fetch('/', {
        method: "PUT",
        body: JSON.stringify({
            post_id: post_id,
            body: body
        })
    });
    p = document.createElement('p');
    p.innerHTML = textarea.value;
    p.id = `c${post_id}`;
    textarea.parentNode.replaceChild(p, textarea);

    saveButton = event.target;
    editButton = document.createElement('button');
    editButton.className = 'btn btn-info';
    editButton.innerHTML = 'Edit';
    editButton.onclick = event => {handleEdit(event)}
    saveButton.parentNode.replaceChild(editButton, saveButton);

}

function handleEdit(event) {
    content = document.querySelector(`#c${event.target.parentElement.id}`);
    textarea = document.createElement('textarea');
    textarea.innerHTML = content.innerHTML;
    textarea.id = `t${event.target.parentElement.id}`;
    textarea.className = 'form-control';
    textarea.style = 'margin-bottom:10px;';
    content.parentNode.replaceChild(textarea, content);

    editButton = event.target;
    saveButton = document.createElement('button');
    saveButton.className = 'btn btn-info';
    saveButton.innerHTML = 'Save';

    post_id = event.target.parentElement.id;
    saveButton.onclick = event => {
        handleSave(post_id, event)
    };
    editButton.parentNode.replaceChild(saveButton, editButton);
}