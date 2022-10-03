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

    var countSelects = document.querySelectorAll('.select').length;
    var name = "clothingItem_id" + countSelects;
    var childSelect = newSelect.childNodes[1];

    childSelect.setAttribute('name', name);
    
    const divSelects = document.querySelector('.selects');
    divSelects.appendChild(newSelect);
}

function removeSelect(event) {
    var countSelects = document.querySelectorAll('.select').length;
    
    if (countSelects != 1)
        event.target.parentNode.parentNode.remove();
}