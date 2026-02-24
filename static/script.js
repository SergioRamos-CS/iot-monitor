const tempCtx = document.getElementById("tempChart").getContext("2d");
const humCtx = document.getElementById("humChart").getContext("2d");

// LIMITES
const TEMP_MIN = 35;
const TEMP_MAX = 40;
const HUM_MIN = 45;
const HUM_MAX = 65;

// GRÁFICO DE TEMPERATURA
const tempChart = new Chart(tempCtx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Temperatura (°C)",
        data: [],
        borderWidth: 2
      },
      {
        label: "Mínimo Ideal",
        data: [],
        borderDash: [5, 5],
        borderWidth: 1
      },
      {
        label: "Máximo Ideal",
        data: [],
        borderDash: [5, 5],
        borderWidth: 1
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false
  }
});

// GRÁFICO DE UMIDADE
const humChart = new Chart(humCtx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Umidade (%)",
        data: [],
        borderWidth: 2
      },
      {
        label: "Mínimo Ideal",
        data: [],
        borderDash: [5, 5],
        borderWidth: 1
      },
      {
        label: "Máximo Ideal",
        data: [],
        borderDash: [5, 5],
        borderWidth: 1
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false
  }
});

async function fetchData() {
  const response = await fetch("/api/data");
  const data = await response.json();

  const labels = data.map(d => d.created_at).reverse();
  const temperatures = data.map(d => d.temperature).reverse();
  const humidities = data.map(d => d.humidity).reverse();

  // VERIFICA LIMITES
  const tempFora = temperatures.some(t => t < TEMP_MIN || t > TEMP_MAX);
  const humFora = humidities.some(h => h < HUM_MIN || h > HUM_MAX);

  // ATUALIZA TEMPERATURA
  tempChart.data.labels = labels;
  tempChart.data.datasets[0].data = temperatures;
  tempChart.data.datasets[0].borderColor = tempFora ? "red" : "blue";
  tempChart.data.datasets[1].data = labels.map(() => TEMP_MIN);
  tempChart.data.datasets[2].data = labels.map(() => TEMP_MAX);

  // ATUALIZA UMIDADE
  humChart.data.labels = labels;
  humChart.data.datasets[0].data = humidities;
  humChart.data.datasets[0].borderColor = humFora ? "red" : "blue";
  humChart.data.datasets[1].data = labels.map(() => HUM_MIN);
  humChart.data.datasets[2].data = labels.map(() => HUM_MAX);

  tempChart.update();
  humChart.update();
}

setInterval(fetchData, 5000);
fetchData();