// Get the button and spinner elements
const button = document.getElementById("myButton");
const spinner = document.getElementById("spinner");

// Add click event listener to the button
button.addEventListener("click", () => {
  // Show the spinner
  showSpinner();

  // Simulate a function that takes time to execute
  setTimeout(() => {
    // Hide the spinner after the function completes
    hideSpinner();
  }, 3000); // Replace 3000 with the actual time your function takes to execute
});

// Function to show the spinner
function showSpinner() {
  spinner.classList.remove("hidden");
}

// Function to hide the spinner
function hideSpinner() {
  spinner.classList.add("hidden");
}