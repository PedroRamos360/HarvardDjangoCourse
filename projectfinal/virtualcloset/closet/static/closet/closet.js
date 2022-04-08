function handleChange(event) {
    var select = event.target;
    var value = select.options[select.selectedIndex].value;
    window.location.href = `/closet?q=${value}`;
}

function handleItemMouseOver(event) {
    var item = event.target;
    item.innerHTML = '';
    item.style.background = '#C850C0';

    var btnAdd = document.createElement('button');
    btnAdd.className = 'btn btn-success';
    btnAdd.id = 'imgbtn';
    btnAdd.style.margin = '0 0 10px 0';
    btnAdd.style.opacity = '100%';
    btnAdd.innerHTML = 'Add to';

    var btnEdit = document.createElement('button');
    btnEdit.className = 'btn btn-warning';
    btnEdit.id = 'imgbtn';
    btnEdit.style.margin = '0 0 10px 0';
    btnEdit.style.opacity = '100%';
    btnEdit.innerHTML = 'Edit';

    var btnDelete = document.createElement('button');
    btnDelete.className = 'btn btn-danger';
    btnDelete.id = 'imgbtn';
    btnDelete.style.opacity = '100%';
    btnDelete.innerHTML = 'Delete';

    item.appendChild(btnAdd);
    item.appendChild(btnEdit);
    item.appendChild(btnDelete);
}

function handleItemMouseOut(event) {
    var item = event.target;
    item.style.background = 'aliceblue';
    var buttons = document.querySelectorAll('#imgbtn');
    buttons.forEach(button => {
        button.remove();
    });
    var new_img = document.createElement('img');
    new_img.src = item.id;
    item.appendChild(new_img);
}

document.addEventListener('DOMContentLoaded', () => {
    var closetpage = document.querySelector('#closetpage');
    closetpage.style.height = `${window.innerHeight -222}px`;
});

window.addEventListener('resize', () => {
    var closetpage = document.querySelector('#closetpage');
    closetpage.style.height = `${window.innerHeight -222}px`;
});
