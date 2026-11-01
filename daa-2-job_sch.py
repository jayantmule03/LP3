# Job Sequencing with Deadlines using Greedy Method

def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max(job[1] for job in jobs)

    # Create empty time slots
    slots = [None] * max_deadline
    total_profit = 0

    # Schedule jobs one by one
    for job in jobs:
        job_id, deadline, profit = job

        # Find the latest available slot before the deadline
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    # Display scheduled jobs and maximum profit
    print("\nScheduled Jobs:", [job for job in slots if job is not None])
    print("Maximum Profit:", total_profit)


# Take input from the user
n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    print(f"\nEnter details for Job {i + 1}:")

    # Job ID: A unique name or number for the job
    job_id = input("Enter Job ID: ")

    # Deadline: Latest time slot by which the job must finish
    deadline = int(input("Enter Deadline: "))

    # Profit: Money earned by completing the job
    profit = int(input("Enter Profit: "))

    # Store each job as (Job ID, Deadline, Profit)
    jobs.append((job_id, deadline, profit))

# Call the function to schedule jobs
job_sequencing(jobs)


# Enter number of jobs: 5

# Enter details for Job 1:
# Enter Job ID: J1
# Enter Deadline: 2
# Enter Profit: 100

# Enter details for Job 2:
# Enter Job ID: J2
# Enter Deadline: 1
# Enter Profit: 19

# Enter details for Job 3:
# Enter Job ID: J3
# Enter Deadline: 2
# Enter Profit: 27

# Enter details for Job 4:
# Enter Job ID: J4
# Enter Deadline: 1
# Enter Profit: 25

# Enter details for Job 5:
# Enter Job ID: J5
# Enter Deadline: 3
# Enter Profit: 15
