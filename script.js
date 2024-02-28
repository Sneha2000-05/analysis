function analyzeSentiment() {
// Get the comments from the textarea
var comments = $('#comments').val();

// Send a request to the server to perform sentiment analysis
$.post('analyze.py', { comments: comments }, function(data) {
// Display the result
$('#result').text(data.result);
});
}