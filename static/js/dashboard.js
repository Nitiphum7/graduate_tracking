document.addEventListener('DOMContentLoaded', function() {
    // Get Dashboard data
    fetch('/api/students/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-students').textContent = data.count;

            const statusCounts = {};
            data.results.forEach(student => {
                const status = student.status_display || 'ไม่ระบุ';
                statusCounts[status] = (statusCounts[status] || 0) + 1;
            });

            const statusLabels = Object.keys(statusCounts);
            const statusData = Object.values(statusCounts);
            const statusColors = ['#4CAF50', '#FFC107', '#2196F3', '#F44336'];

            new Chart(document.getElementById('student-status-chart'), {
                type: 'pie',
                data: {
                    labels: statusLabels,
                    datasets: [{
                        data: statusData,
                        backgroundColor: statusColors
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'right' }
                    }
                }
            });
        });

    fetch('/api/advisors/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-advisors').textContent = data.count;
        });

    fetch('/api/programs/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-programs').textContent = data.count;

            const programIds = data.results.map(p => p.id);
            const programNames = data.results.map(p => p.name);
            const studentCountsByProgram = Array(programIds.length).fill(0);

            Promise.all(programIds.map(id =>
                fetch(`/api/students/?program=${id}`)
                    .then(res => res.json())
                    .then(data => data.count)
            )).then(counts => {
                for (let i = 0; i < counts.length; i++) {
                    studentCountsByProgram[i] = counts[i];
                }

                new Chart(document.getElementById('student-program-chart'), {
                    type: 'bar',
                    data: {
                        labels: programNames,
                        datasets: [{
                            label: 'จำนวนนักศึกษา',
                            data: studentCountsByProgram,
                            backgroundColor: '#3F51B5'
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true,
                                precision: 0
                            }
                        }
                    }
                });
            });
        });

    fetch('/api/thesis-proposals/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-theses').textContent = data.count;

            const activeTheses = data.results.filter(thesis =>
                thesis.status === 'pending' || thesis.status === 'passed_with_revision'
            );

            const tableBody = document.querySelector('#active-theses-table tbody');
            tableBody.innerHTML = '';

            if (activeTheses.length === 0) {
                tableBody.innerHTML = '<tr><td colspan="6" class="text-center">ไม่พบข้อมูลวิทยานิพนธ์ที่กำลังดำเนินการ</td></tr>';
                return;
            }

            activeTheses.forEach(thesis => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${thesis.student.student_id}</td>
                    <td>${thesis.student.user.first_name} ${thesis.student.user.last_name}</td>
                    <td>${thesis.title}</td>
                    <td>${thesis.student.advisor ? thesis.student.advisor.user.first_name + ' ' + thesis.student.advisor.user.last_name : '-'}</td>
                    <td><span class="badge bg-${thesis.status === 'pending' ? 'warning' : 'info'}">${thesis.status_display}</span></td>
                    <td><a href="/theses/${thesis.id}/" class="btn btn-sm btn-primary"><i class="fas fa-eye"></i> ดูรายละเอียด</a></td>
                `;
                tableBody.appendChild(row);
            });
        });
});
