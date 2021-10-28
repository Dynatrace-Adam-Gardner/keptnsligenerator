from num2words import num2words
import yaml

print("Starting Keptn SLI File Generator...")

slis = {
  "spec_version": "1.0",
  "indicators": {}
}

# Build Stages
number_of_slis = None
while number_of_slis is None:
  number_of_slis = input("How many SLIs do you want to define? ")

  try:
    number_of_slis = int(number_of_slis)
  except:
    number_of_slis = None
    print('Got an invalid number of SLIs. Please use numbers. Try again...')

count = 1
while count <= number_of_slis:
  ordinal = num2words(count, to="ordinal_num")
  sli_name = input(f"Please enter the name of your {ordinal} SLI: ")
  sli_definition = input(f"Please enter the definition for {sli_name}: ")

  #sli_list.append({ sli_name: sli_definition})
  slis['indicators'][sli_name] = sli_definition
  count += 1

# Done. Print output
print('\n')
print('Output follows. Save this as sli.yaml')
print('Upload this to Git to the relevant: <stageName>/<serviceName>/prometheus/sli.yaml')
print('Alternatively, upload using keptn cli: keptn add-resource --project=<projectName> --stage=<stageName> --service=<serviceName> --resource=sli.yaml --resourceUri=<monitoringProvider>/sli.yaml')
print('\n\n')
print('---')
print(yaml.dump(slis))
print('\n')
