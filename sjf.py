def sjf_scheduling(processes):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n

    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    print("Scheduling using SJF (Non-Preemptive):\n")

    while completed != n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            pid, at, bt = processes[i]
            if at <= current_time and not is_completed[i]:
                if bt < min_bt:
                    min_bt = bt
                    idx = i
                elif bt == min_bt:
                    if at < processes[idx][1]:
                        idx = i

        if idx != -1:
            pid, at, bt = processes[idx]
            current_time += bt
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - at
            waiting_time[idx] = turnaround_time[idx] - bt
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1  # Idle CPU

    # Calculate averages
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n

    # Output results
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        pid, at, bt = processes[i]
        print(f"{pid}\t{at}\t{bt}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
    print(f"Average Waiting Time = {avg_wt:.2f}")

# Example usage:
process_list = [
    ("P1", 0, 7),
    ("P2", 2, 4),
    ("P3", 4, 2),
    ("P4", 7, 1)
]

sjf_scheduling(process_list)
