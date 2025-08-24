// Function to update the dashboard data
function updateDashboardData() {
    fetch('/update_data')
        .then(response => response.json())
        .then(data => {
            // In a real application, you would update the DOM elements with the new data
            console.log('Dashboard data updated:', data);
            
            // Example: Update the attack stats list
            const attackStatsList = document.querySelector('.list-group');
            if (attackStatsList) {
                attackStatsList.innerHTML = '';
                for (const [attack, count] of Object.entries(data.attack_stats)) {
                    const item = document.createElement('div');
                    item.className = 'list-group-item list-group-item-action bg-secondary text-white mb-1 d-flex justify-content-between align-items-center';
                    item.innerHTML = `
                        ${attack}
                        <span class="badge bg-primary rounded-pill">${count}</span>
                    `;
                    attackStatsList.appendChild(item);
                }
            }
            
            // Example: Update the attack chart
            const attackChartImg = document.querySelector('.card-body.text-center img');
            if (attackChartImg) {
                attackChartImg.src = `data:image/png;base64,${data.attack_chart}`;
            }
        })
        .catch(error => console.error('Error updating dashboard data:', error));
}

// Auto-refresh data every 30 seconds
setInterval(updateDashboardData, 30000);

// Initialize the dashboard
document.addEventListener('DOMContentLoaded', function() {
    // Any initialization code can go here
    console.log('Dashboard initialized');
    
    // Example: Add click event to malicious IPs for quick mitigation
    document.querySelectorAll('table tbody tr').forEach(row => {
        row.addEventListener('click', function() {
            const ip = this.cells[0].textContent;
            document.getElementById('ip_address').value = ip;
        });
    });
});