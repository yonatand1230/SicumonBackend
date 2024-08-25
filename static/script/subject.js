function getQuery() {
    const url = window.location.search;
    const urlParams = new URLSearchParams(url);
    const params = {};
    for (const [key, value] of urlParams) {
      params[key] = value;
    }
    return params;
  }

function loadTitle() {
    fetch('files/subjects.json')
    .then(
        (response) => {
            return response.json();
        }
    ).then((subjectJson) => {
        const titleElement = document.getElementById('title-h1');
        const engSubject = getQuery()['subject'];
        const subjects = subjectJson['subjects'];
        for(sub of subjects) {
            if (sub.eng==engSubject) {
                titleElement.textContent = sub.name;
                document.title += " | "+sub.name;
            }
        }
    });
}