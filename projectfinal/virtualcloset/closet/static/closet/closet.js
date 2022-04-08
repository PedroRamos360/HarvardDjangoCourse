function handleChange(event) {
    var select = event.target;
    var value = select.options[select.selectedIndex].value;
    window.location.href = `/closet?q=${value}`;
}