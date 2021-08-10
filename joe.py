import sys
import requests

n_tries = int(sys.argv[1])
test_urls = sys.argv[2:]

results = { test_url: 0 for test_url in test_urls }

print('Running requests:')

for test_url in test_urls:
  counter = 0
  for i in range(n_tries):
    print(f'\t[GET] {test_url}: {i+1}/{n_tries}', end='\r')
    response = requests.get(test_url)
    counter += response.elapsed.total_seconds()
  results[test_url] = counter / n_tries
  print()

print(f'\nResults averaged over {n_tries} tries for each endpoint:')
for test_url in results:
  print(f'\t{test_url}: {int(results[test_url]*1000)}ms')