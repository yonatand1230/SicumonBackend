function showOptions() {
    var modal = document.getElementsByClassName('modal')[0];
    modal.classList.add('open');
}

function closeOptions() {
    var modal = document.getElementsByClassName('modal')[0];
    modal.classList.remove('open');
}

function updateGrade() {
    const selector = document.getElementById('grade-selector');
    const grade = selector.options[selector.selectedIndex].value;
    document.cookie=("grade="+grade);
}