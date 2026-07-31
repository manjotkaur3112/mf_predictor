const data = window.fundGraph;

new Chart(document.getElementById("fundChart"), {
    type: "line",

    data: {
        labels: data.labels,
        datasets: [{
            label: "Fund Return (%)",
            data: data.values,
            borderColor: "rgb(163, 135, 22)",
            backgroundColor: "rgba(163, 135, 22, 0.2)",
            borderWidth: 3,
            fill: true,
            tension: 0.4,
            pointRadius: 5,
            pointBackgroundColor: "rgba(163, 135, 22, 0.2)"
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 20
                    },
                    color: "#ffffff"
                }
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: "Investment Period"
                }
            },
            y: {
                title: {
                    display: true,
                    text: "Return (%)"
                },
                beginAtZero: true
            }
        }
    }
});