# parsing the git log and outputting a pandas df for further analysis
# use by running the script in the location of the git log

import subprocess
import pandas as pd

# Run git log command and save the output
cmd_str = 'git log --pretty=format:"%an|%ad|%ae|%s"'
git_log = subprocess.run([cmd_str], shell=True, stdout=subprocess.PIPE).stdout.decode('ISO-8859-1')


# Split output into lines, parse lines and split into 4 components
log_lines = git_log.strip().split('\n')
data = []
for line in log_lines:
    message, email, date, author = line.rsplit('|', 3)
    data.append({'Message': message.strip(), 'Email': email.strip(), 'Date': date.strip(), 'Author': author.strip()})


# Create dataframe and rename colunms
df = pd.DataFrame(data)
df.columns = ['Author', 'Date', 'Email', 'Message']


# Save df into cvs
df.to_csv('git_log.csv', index=False)

