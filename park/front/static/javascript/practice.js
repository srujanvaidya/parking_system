function getCSRFToken() {
  return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

// Attach listeners after DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  const parkForm = document.getElementById("parkForm");
  const departForm = document.getElementById("departForm");

  // Change this base URL to your backend API
  const API_BASE = "http://127.0.0.1:8000";

  // Park vehicle
  parkForm.addEventListener("submit", async (e) => {
    e.preventDefault(); // prevent page reload
    const carno = document.getElementById("licensePlatePark").value;

    try {
      const response = await fetch(`${API_BASE}/api/park/input/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({ carno }),
      });
      const data = await response.json();
      if (response.ok) {
        alert(`✅ Vehicle parked successfully!\nSlot: ${data.slot}`);
      } else {
        alert(`❌ Error: ${data.message || "Unable to park vehicle."}`);
      }
    } catch (err) {
      console.error(err);
      alert("⚠️ Server not reachable. Check your backend.");
    }
  });

  // Depart vehicle
  departForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const carno = document.getElementById("licensePlateDepart").value;

    try {
      const response = await fetch(`${API_BASE}/api/park/exit/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({ carno }),
      });
      const data = await response.json();
      if (response.ok) {
        alert(`🚗 Vehicle departed!\nFees: ${data.fee || "N/A"}`);
      } else {
        alert(`❌ Error: ${data.message || "Unable to depart vehicle."}`);
      }
    } catch (err) {
      console.error(err);
      alert("⚠️ Server not reachable. Check your backend.");
    }
  });

  // Exit system
  const exitButton = document.getElementById("exit-button");
  exitButton.addEventListener("click", async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${API_BASE}/exit/`, { method: "POST" });
      if (response.ok) {
        alert("👋 System closed successfully.");
      } else {
        alert("❌ Error closing the system.");
      }
    } catch (err) {
      console.error(err);
      alert("⚠️ Server not reachable. Check your backend.");
    }
  });
});
