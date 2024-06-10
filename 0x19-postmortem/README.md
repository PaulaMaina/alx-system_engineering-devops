# Project Postmortem: May 9th, 2024 Outage

## Issue Summary

**Duration of the Outage:**  
Start: May 9th, 2024, 08:30 AM (EAT)  
End: May 9th, 2024, 11:45 AM (EAT)  
Total Duration: 3 hours and 15 minutes

**Impact:**  
Our primary e-commerce service was significantly slowed. Users experienced long load times when accessing the website; some pages failed to load entirely. Approximately 40% of users were affected during the outage. Imagine waiting for a page to load longer than it takes to brew a cup of coffee!

**Root Cause:**  
The root cause was a misconfiguration in our load balancer that caused an uneven distribution of traffic, overloading some servers while others took an unexpected coffee break.

## Timeline

- **08:30 AM:** Issue detected via automated monitoring alerts indicating increased response times and error rates. The alarms screamed like they saw a spider.
- **08:35 AM:** Initial investigation by on-call engineer confirmed the alerts. Time to grab a big cup of coffee.
- **08:45 AM:** Assumed cause to be a database bottleneck; investigation into database logs and performance began. After all, the database is usually the usual suspect.
- **09:15 AM:** Database team identified no significant issues; hypothesis shifted to potential networking issues. Nothing like chasing ghosts in the wires!
- **09:45 AM:** Networking team ruled out internal network problems; escalated to the infrastructure team. Pass the mystery up the chain!
- **10:00 AM:** The Infrastructure team noticed irregularities in load balancer traffic patterns. Aha! A clue in the game of network detective!
- **10:30 AM:** Misconfiguration in load balancer identified as root cause. Bingo! We found the culprit sneaking around in our load balancer settings.
- **11:00 AM:** Load balancer configuration corrected. Servers rejoiced and stopped grumbling.
- **11:45 AM:** Monitoring confirmed that service levels returned to normal. The internet is happy again.

## Root Cause and Resolution

**Detailed Explanation of the Cause:**  
The load balancer was configured incorrectly during a recent update, leading to an uneven distribution of traffic. Some servers received an excessive number of requests, causing them to become overloaded, while others were underutilized and had the chance to catch up on their reading.

**Detailed Explanation of the Fix:**  
The load balancer configuration was reviewed and corrected to ensure an even distribution of traffic across all servers. Specifically, the weight values for the load balancer pools were adjusted to balance the incoming requests more evenly. Following this, a series of load tests were conducted to confirm that the distribution was functioning correctly. No more lazy servers on our watch!

## Corrective and Preventative Measures

**Improvements and Fixes:**

1. **Load Balancer Configuration Review:** Implement a more rigorous review process for changes to load balancer configurations to catch misconfigurations before they are deployed. No more surprises!
2. **Enhanced Monitoring:** Add more detailed monitoring for load balancer performance, including alerts for uneven traffic distribution. Think of it as traffic cops for our servers.
3. **Automated Load Tests:** Implement automated load testing as part of our deployment pipeline to detect potential issues before they affect production. Stress-testing our servers so they don't stress us.

**List of Tasks:**

- **Task 1:** Develop a checklist for load balancer configuration changes and enforce its use during all updates. Checklists: not just for astronauts!
- **Task 2:** Enhance monitoring tools to include detailed metrics on load balancer traffic distribution. Because knowledge is power.
- **Task 3:** Integrate automated load tests into the CI/CD pipeline to ensure new configurations are tested under load conditions. Ready, set, test!
- **Task 4:** Conduct training sessions for the infrastructure team on best practices for load balancer configuration and traffic management. A well-trained team is a happy team.

