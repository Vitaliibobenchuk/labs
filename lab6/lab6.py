def calculate_estimate(a, m, b):
  E = (a + 4 * m + b) / 6 
  SD = (b - a) / 6 
  return E, SD 
def calculate_project_interval(tasks):
    total_E = 0 
    total_SE = 0 
    for task in tasks:
      a, m, b = task 
      E, SD = calculate_estimate(a, m, b) 
      total_E += E 
      total_SE += SD

  project_E = total_E
  project_SE = total_SE

  project_CI_min = project_E - 2 * project_SE
  project_CI_max = project_E + 2 * project_SE
  return project_CI_min,project_CI_max 

num_tasks = int(input("Введіть кількість завдань: ")) 
tasks = [] for i in range(num_tasks): 
  a = float(input("Введіть оцінку a для завдання {}: ".format(i+1))) 
  m = float(input("Введіть оцінку m для завдання {}: ".format(i+1))) 
  b = float(input("Введіть оцінку b для завдання {}: ".format(i+1))) 
  tasks.append((a, m, b)) 
  project_CI_min, project_CI_max = calculate_project_interval(tasks) 
  print("Project's 95% confidence interval: {} ... {} points".format(project_CI_min, project_CI_max))
