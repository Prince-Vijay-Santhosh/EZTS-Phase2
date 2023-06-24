#implementation of forest(set of tree)
families={
          'charley':{'sam':{'Boxy','rosy'},'nila':{'tae'}},
          'satish':{'Akash','Harsha','vasrha'},
          'bts':{'rm':{'v','jk'},'jin':{'jimin','jhope','suga'}}
         }
for parent,children in families.items():
    print(f"{parent} has {len(children)}kid(s):")
    print(f" {',and '.join([str(child) for child in[*children]])}")
          
          