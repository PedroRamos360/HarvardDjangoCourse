document.addEventListener('DOMContentLoaded', () => {
    var lookspage = document.querySelector('#lookspage');
    lookspage.style.height = `${window.innerHeight -132}px`;
});

window.addEventListener('resize', () => {
    var lookspage = document.querySelector('#lookspage');
    lookspage.style.height = `${window.innerHeight -132}px`;
});

function addSelect() {
    var firstselect = document.querySelector('.select');
    var newSelect = firstselect.cloneNode(true);
    const divSelects = document.querySelector('.selects');
    divSelects.appendChild(newSelect);
}

function removeSelect(event) {
    event.target.parentNode.parentNode.remove();
}