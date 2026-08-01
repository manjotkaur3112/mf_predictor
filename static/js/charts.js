const graphElement = document.getElementById("graph-data");

if (!graphElement) {
    console.log("graph-data element not found.");
} else {

    const graphData = JSON.parse(graphElement.textContent);

    // Average Returns
    if (graphData.average_returns && document.getElementById("avgChart")) {

        const avg = graphData.average_returns;

        new Chart(document.getElementById("avgChart"), {
            type: "line",
            data: {
                labels: avg.labels,
                datasets: [{
                    label: "Average Return %",
                    data: avg.values,
                    borderWidth: 3,
                    fill: false
                }]
            }
        });

    }

    // Expense Ratio
    if (graphData.expense_ratio && document.getElementById("expenseChart")) {

        const expense = graphData.expense_ratio;

        new Chart(document.getElementById("expenseChart"), {
            type: "bar",
            data: {
                labels: expense.labels,
                datasets: [{
                    label: "Expense Ratio %",
                    data: expense.values
                }]
            }
        });

    }

    // Risk Return
    if (graphData.risk_return && document.getElementById("riskChart")) {

        const risk = graphData.risk_return;

        new Chart(document.getElementById("riskChart"), {
            type: "scatter",
            data: {
                datasets: [{
                    label: "Risk Return %",
                    data: risk.x.map((x, i) => ({
                        x: x,
                        y: risk.y[i]
                    }))
                }]
            }
        });

    }

    // Classification
    if (graphData.classification && document.getElementById("classChart")) {

        const cls = graphData.classification;

        new Chart(document.getElementById("classChart"), {
            type: "bar",
            data: {
                labels: cls.labels,
                datasets: [{
                    label: "Classification",
                    data: cls.values
                }]
            }
        });

    }
}