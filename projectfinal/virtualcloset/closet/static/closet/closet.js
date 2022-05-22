function handleChange(event) {
    var select = event.target;
    var value = select.options[select.selectedIndex].value;
    window.location.href = `/closet?q=${value}`;
}

function handleItemMouseOver(event) {
    if (event.target.id != "imgbtn") {
        var id = event.target.id;
        var buttonDiv = document.querySelector(`#btn${id.substring(3)}`);
        buttonDiv.style.display = "flex";
        event.target.style.display = "none";
    }
}

function handleItemMouseOut(event) {
    if (event.target.id != "imgbtn") {
        var id = event.target.id;
        var imageDiv = document.querySelector(`#img${id.substring(3)}`);
        imageDiv.style.display = "flex";
        event.target.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', () => {
    var closetpage = document.querySelector('#closetpage');
    closetpage.style.height = `${window.innerHeight -202}px`;
});

window.addEventListener('resize', () => {
    var closetpage = document.querySelector('#closetpage');
    closetpage.style.height = `${window.innerHeight -202}px`;
});
