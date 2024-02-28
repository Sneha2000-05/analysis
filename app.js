document.getElementById('comment-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const comment = document.getElementById('comment').value;

    const commentsDiv = document.getElementById('comments');
    const newComment = document.createElement('div');
    newComment.innerHTML = `<strong>${name}:</strong> ${comment}`;
    commentsDiv.appendChild(newComment);

    document.getElementById('comment').value = '';
});