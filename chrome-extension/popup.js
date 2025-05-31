document.getElementById("downloadBtn").addEventListener("click", () => {
  const url = document.getElementById("videoUrl").value.trim();
  const quality = document.getElementById("quality").value;
  const status = document.getElementById("status");

  if (!url) {
    status.textContent = "Please enter a URL.";
    return;
  }

  status.textContent = "Downloading...";

  fetch("https://your-app-name.onrender.com/download", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url, quality })
  })
  .then(response => {
    if (!response.ok) throw new Error("Download failed");
    return response.blob();
  })
  .then(blob => {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "video.mp4";
    a.click();
    status.textContent = "Download complete.";
  })
  .catch(err => {
    status.textContent = "Download failed: " + err.message;
  });
});
