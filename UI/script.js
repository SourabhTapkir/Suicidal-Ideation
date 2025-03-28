// Ensure the DOM content is fully loaded before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {
  const postButton = document.querySelector('.tweet-actions button'); // Select the Post button
  const tweetBox = document.querySelector('#tweet-box'); // Select the textarea for tweets
  const feed = document.querySelector('.feed'); // Select the feed container

  // Add a click event listener to the Post button
  postButton.addEventListener('click', async () => {
    console.log("Post button clicked"); // Debug log to ensure the button click is detected

    const tweetContent = tweetBox.value.trim(); // Get the content of the tweet and trim whitespace
    console.log("Tweet Content:", tweetContent); // Debug log to show the input tweet content

    if (tweetContent) {
      // Create a new tweet element
      const newTweet = document.createElement('div');
      newTweet.className = 'tweet';
      newTweet.innerHTML = `
        <h4><strong>Sourabh Tapkir</strong></h4>
        <p>${tweetContent}</p>
        <p class="stats">0 Likes • 0 Retweets</p>
      `;
      feed.prepend(newTweet); // Add the new tweet to the top of the feed
      tweetBox.value = ''; // Clear the tweet box after posting

      try {
        // Send the tweet content to the prediction service
        const response = await fetch('http://127.0.0.1:5000/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ tweet: tweetContent }), // Send tweet as JSON
        });

        console.log("Fetch request sent"); // Debug log to confirm the request was sent

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`); // Handle non-OK responses
        }

        const data = await response.json(); // Parse the JSON response
        console.log("Prediction Response:", data); // Debug log to show the prediction response

        const result = data.prediction; // Get the prediction result
        if (result === 'Suicidal Ideation') {
          console.log("Redirecting to recommendations page"); // Debug log for redirection
          window.location.href = '/recommendations.html'; // Redirect to the recommendations page
        } else {
          // Show the prediction result under the new tweet
          const resultBox = document.createElement('div');
          resultBox.className = 'tweet-result';
          resultBox.innerHTML = `<p>Prediction: <strong>${result}</strong></p>`;
          newTweet.appendChild(resultBox);
        }
      } catch (error) {
        // Handle errors during the fetch call
        console.error('Error during prediction service:', error.message);
        alert('There was an error with the prediction service.');
      }
    } else {
      // Handle empty tweet input
      alert('Please enter some text!');
    }
  });
});
