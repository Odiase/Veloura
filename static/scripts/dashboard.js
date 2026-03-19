// // Monthly Revenue Chart
// new Chart(document.getElementById("revenueChart"), {
//     type: "line",
//     data: {
//         labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
//         datasets: [{
//             label: "Revenue ($)",
//             data: [4200, 5200, 6100, 7000, 6500, 7400, 8200, 8800, 9400, 10300, 11100, 12400],
//             borderWidth: 3,
//             fill: true
//         }]
//     }
// });


// // Sales Distribution Pie
// new Chart(document.getElementById("salesPie"), {
//     type: "pie",
//     data: {
//         labels: ["Makeup", "Skincare", "Haircare"],
//         datasets: [{
//             data: [45, 35, 20]
//         }]
//     }
// });


// // Orders Per Month
// new Chart(document.getElementById("ordersChart"), {
//     type: "bar",
//     data: {
//         labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
//         datasets: [{
//             label: "Orders",
//             data: [120, 150, 180, 210, 260, 300, 340, 390]
//         }]
//     }
// });


// // Category Performance
// new Chart(document.getElementById("categoryChart"), {
//     type: "doughnut",
//     data: {
//         labels: ["Lipstick", "Foundation", "Perfume", "Face Cream"],
//         datasets: [{
//             data: [30, 25, 20, 25]
//         }]
//     }
// });


// new Chart(document.getElementById("roiChart"), {
//     type: "line",
//     data: {
//         labels: ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"],
//         datasets: [
//             {
//                 label: "Investment",
//                 data: [8000, 8000, 8000, 8000, 8000, 8000],
//                 borderWidth: 2
//             },
//             {
//                 label: "Revenue Growth",
//                 data: [5000, 9000, 15000, 22000, 34000, 48240],
//                 borderWidth: 3
//             }
//         ]
//     }
// });

// dashboard.js

// Keep track of charts so we can destroy them before re-rendering
let revenueChart, ordersChart, salesPie, roiChart, categoryChart;

async function loadDashboard() {
    const response = await fetch("/dashboard/api/");
    const data = await response.json();

    // Update metric cards
    document.getElementById("totalRevenue").innerText = `$${data.total_revenue}`;
    document.getElementById("totalOrders").innerText = data.total_orders;
    document.getElementById("totalCustomers").innerText = data.total_customers;
    document.getElementById("conversionRate").innerText = `${data.conversion_rate}%`;
    document.getElementById("avgOrderValue").innerText = `$${data.avg_order_value}`;
    document.getElementById("businessAge").innerText = `${data.business_age} Months`;

    // Destroy old charts if they exist
    if (revenueChart) revenueChart.destroy();
    if (ordersChart) ordersChart.destroy();
    if (salesPie) salesPie.destroy();
    if (roiChart) roiChart.destroy();
    if (categoryChart) categoryChart.destroy();

    // Revenue Chart
    // revenueChart = new Chart(document.getElementById("revenueChart"), {
    //     type: "line",
    //     data: {
    //         labels: data.monthly_revenue.map((_, i) => `Month ${i + 1}`),
    //         datasets: [{
    //             label: "Revenue ($)",
    //             data: data.monthly_revenue,
    //             borderWidth: 3,
    //             fill: true,
    //             borderColor: "#d63384",
    //             backgroundColor: "rgba(214,51,132,0.2)"
    //         }]
    //     }
    // });
    revenueChart = new Chart(document.getElementById("revenueChart"), {
        type: "line",
        data: {
            labels: ["Month 1", "Month 2", "Month 3"],
            datasets: [{
                label: "Revenue ($)",
                data: [900, 1580, 2450],
                borderWidth: 3,
                fill: true
            }]
        }
    });


    // Orders per Month
    ordersChart = new Chart(document.getElementById("ordersChart"), {
        type: "bar",
        data: {
            labels: data.monthly_orders.map((_, i) => `Month ${i + 1}`),
            datasets: [{
                label: "Orders",
                data: data.monthly_orders,
                backgroundColor: "#0d6efd"
            }]
        }
    });

    // Category Revenue Pie
    salesPie = new Chart(document.getElementById("salesPie"), {
        type: "pie",
        data: {
            labels: Object.keys(data.category_revenue),
            datasets: [{
                data: Object.values(data.category_revenue_percent),
                backgroundColor: ["#d63384", "#0d6efd", "#ffc107"]
            }]
        }
    });

    // ROI Chart
    // roiChart = new Chart(document.getElementById("roiChart"), {
    //     type: "line",
    //     data: {
    //         labels: data.monthly_revenue.map((_, i) => `Month ${i + 1}`),
    //         datasets: [
    //             {
    //                 label: "Initial Investment",
    //                 data: Array(data.monthly_revenue.length).fill(data.investment),
    //                 borderWidth: 2,
    //                 borderColor: "#555",
    //                 fill: false
    //             },
    //             {
    //                 label: "Revenue Growth",
    //                 data: data.monthly_revenue,
    //                 borderWidth: 3,
    //                 borderColor: "#d63384",
    //                 fill: false
    //             }
    //         ]
    //     }
    // });
    roiChart = new Chart(document.getElementById("roiChart"), {
         type: "line",
         data: {
             labels: ["Month 1", "Month 2", "Month 3"],
             datasets: [
                 {
                     label: "Target",
                     data: [3000, 3000, 3000, 3000, 3000, 3000],
                     borderWidth: 2
                 },
                 {
                     label: "Revenue Growth",
                     data: [900, 1580, 2450],
                     borderWidth: 3
                 }
             ]
         }
         });

        // Category Orders Doughnut
        categoryChart = new Chart(document.getElementById("categoryChart"), {
            type: "doughnut",
            data: {
                labels: Object.keys(data.category_orders),
                datasets: [{
                    data: Object.values(data.category_orders_percent),
                    backgroundColor: ["#d63384", "#0d6efd", "#ffc107", "#28a745"]
                }]
            }
        });
    }

loadDashboard();