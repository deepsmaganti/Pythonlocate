import unicodecsv

def read_csv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

# ## printing the first row

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

# print enrollments[0]
# print daily_engagement[0]
# print project_submissions[0]

# ## Get number of rows in the table

# print len(enrollments)
# print len(daily_engagement)
# print len(project_submissions)
unique_val = set()
def unique_func(tablename,unique_coln):
    for i in tablename:
        unique_val.add(i[unique_coln])
    return unique_val

## Get number of unique students
# print unique_func(enrollments, 'account_key')
# print unique_func(daily_engagement, 'acct')
# print unique_func(project_submissions, 'account_key')

## Problems in Data - daily engagement account_key coln name is differnt and number of unique students in enrollments and engagement is differnt

## Fixing account_key coln name

for eachrow in daily_engagement:
    eachrow['account_key'] = eachrow['acct']
    del eachrow['acct']
## print daily_engagement[0]

u_student = unique_func(daily_engagement,'account_key')
extra_students_enroll = set()
for i in enrollments:
    student = i['account_key']
    if student not in u_student and i['join_date'] != i['cancel_date']:
        print i
print len(extra_students_enroll)
