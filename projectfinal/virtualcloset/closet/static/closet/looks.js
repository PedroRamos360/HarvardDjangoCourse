document.addEventListener('DOMContentLoaded', () => {
    var lookspage = document.querySelector('#lookspage');
    lookspage.style.height = `${window.innerHeight -132}px`;
});

window.addEventListener('resize', () => {
    var lookspage = document.querySelector('#lookspage');
    lookspage.style.height = `${window.innerHeight -132}px`;
});