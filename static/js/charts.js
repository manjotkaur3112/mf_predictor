const graphData = JSON.parse(
    document.getElementById("graph-data").textContent
);



const avg = graphData.average_returns;

new Chart(document.getElementById("avgChart"),{

    type:"line",

    data:{
        labels:avg.labels,

        datasets:[{
            label:"Average Return %",
            data:avg.values,
            borderWidth:3,
            fill:false
        }]
    },

    options:{
        responsive:true,
        maintainAspectRatio:false,
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 20
                    },
                    color: "#ffffff"
                }
            }
        }
    }

});


const expense = graphData.expense_ratio;

new Chart(document.getElementById("expenseChart"),{

    type:"bar",

    data:{
        labels:expense.labels,

        datasets:[{
            label:"Expense Ratio %",
            data:expense.values
        }]
    },

    options:{
        responsive:true,
        maintainAspectRatio:false,
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 20
                    },
                    color: "#ffffff"
                }
            }
        }
    }

});


const risk = graphData.risk_return;

new Chart(document.getElementById("riskChart"),{

    type:"scatter",

    data:{
        datasets:[{
            label:"Risk Return %",
            data:risk.x.map((x,i)=>({
                x:x,
                y:risk.y[i]
            }))
        }]
    },

    options:{
        responsive:true,
        maintainAspectRatio:false,
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 20
                    },
                    color: "#ffffff"
                }
            }
        }
    }

});


const cls = graphData.classification;

new Chart(document.getElementById("classChart"),{

    type:"bar",

    data:{
        labels:cls.labels,

        datasets:[{
            label:"Classification Chart %",
            data:cls.values
        }]
    },

    options:{
        responsive:true,
        maintainAspectRatio:false,
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 20
                    },
                    color: "#ffffff"
                }
            }
        }
    }

});
