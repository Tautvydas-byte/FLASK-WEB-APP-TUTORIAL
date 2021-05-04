function deleteNote(noteId){
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";//refresh/reload home window
    });
}
//take note ID than we pass, send POST to /delete-note request, then after repsonse reload the window