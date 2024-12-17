console.log("this is js from home page haha");

let startTime;
let timerInterval;

const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopButton");

const hoursDisplay = document.getElementById("hours");
const minutesDisplay = document.getElementById("minutes");
const secondsDisplay = document.getElementById("seconds");

startButton.addEventListener("click", () => {
  //alert("start button clicked");
  startTime = new Date();
  timerInterval = setInterval(updateElapsedTime, 1000);
  startButton.classList.remove("active");
  startButton.classList.add("inactive");
  stopButton.classList.remove("inactive");
  stopButton.classList.add("active");

  startButton.disabled = true;
  stopButton.disabled = false;
});

stopButton.addEventListener("click", () => {
  //alert("stop button clicked");
  clearInterval(timerInterval);
  timerInterval = null;

  stopButton.classList.remove("active");
  stopButton.classList.add("inactive");
  startButton.classList.remove("inactive");
  startButton.classList.add("active");

  startButton.disabled = false;
  stopButton.disabled = true;
  const now = new Date();
  saveSessionData(now);
});

function saveSessionData(stopTime) {
  const date = startTime.toISOString().split("T")[0]; // Format: YYYY-MM-DD
  const start_time = startTime.toTimeString().split(" ")[0]; // Format: HH:MM:SS
  const end_time = stopTime.toTimeString().split(" ")[0]; // Format: HH:MM:SS
  const project = document.getElementById("project").value;
  const userId = document.getElementById("userID").value;

  const data = {
    //id: 15, // Replace with actual ID logic if needed
    user: userId, // Replace with the actual user ID
    project: project, // Replace with the actual project ID
    date: date,
    start_time: start_time,
    end_time: end_time,
  };
  console.log(data);

  fetch("http://127.0.0.1:8000/traker/api/time-entries/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (response.ok) {
        alert("Session data saved successfully!");
      } else {
        throw new Error("Failed to save session data");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Error saving session data");
    });
}

function updateElapsedTime() {
  const now = new Date();
  const elapsed = new Date(now - startTime); // Time difference in milliseconds

  const hours = String(elapsed.getUTCHours()).padStart(2, "0");
  const minutes = String(elapsed.getUTCMinutes()).padStart(2, "0");
  const seconds = String(elapsed.getUTCSeconds()).padStart(2, "0");
  //const timeString = `${hours}:${minutes}:${seconds}`;

  hoursDisplay.textContent = hours;
  minutesDisplay.textContent = minutes;
  secondsDisplay.textContent = seconds;
}
