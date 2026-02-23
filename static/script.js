const ctx = document.getElementById("chart");

async function loadData() {
  const response = await fetch("/api/data");
  const data = await response.json();

  const labels = data.map((d) => d.created_at).reverse();
  const temps = data.map((d) => d.temperature).reverse();

  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Temperatura (°C)",
          data: temps,
        },
      ],
    },
  });
}

loadData();
setInterval(loadData, 5000);
