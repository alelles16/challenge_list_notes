fetch("/notes/api/")
.then(response => response.json())
.then(data => {
    let notesList = document.getElementById("notesList");

    let html = "";
    data.forEach(note => {
        html += `
            <li class="list-group-item d-flex justify-content-between lh-sm">
                <div>
                    <h6 class="my-0">${note.title}</h6>
                    <small class="text-body-secondary">${note.content}</small>
                </div>
            </li>`;
    });

    notesList.innerHTML = html;
})
.catch(error => console.error("Error:", error));
