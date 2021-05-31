import sys
import os
import modelc
import modeld

print(os.getcwd())

print("Argument Length is: ", len(sys.argv))
if int(sys.argv[1]) == 0:
    model_type = sys.argv[1]
    mod_layer_count = sys.argv[2]
    mod_layer_data_string = sys.argv[3]
    print(mod_layer_data_string)

    mod_data_list = mod_layer_data_string.split("],")
    d = [i.strip('[') for i in mod_data_list]
    d = [i.strip(']') for i in d]
    print(d)
    final_data_list = []
    for i in range(len(d)):
        final_data_list.append(list(d[i].split(",")))
    epochs = sys.argv[4]
    '''
    model_type = 0
    mod_layer_count = 3
    final_data_list = [[12,8,'relu'],[8,4,'sigmoid'],[4,2,'sigmoid']]
    epochs = 10
    '''
    mod = modelc.model_class(
        model_type, mod_layer_count, final_data_list, epochs)

    print("MADE THE MODEL!!!")
    #csv_file = pd.read_csv("EURUSD1.csv")
    # print(csv_file)
    mod.model_run('EURUSD1.csv', 'Target')

    print("RAN THE MODEL!!!")
    #target_model = modelc.model()
elif int(sys.argv[1]) == 1:
    mod = modeld.modeld_class()
    if sys.argv[2] == "None":
        mod.max_depth = None
    else:
        mod.max_depth = int(sys.argv[2])
    if sys.argv[3] == "None":
        mod.max_depth = None
    else:
        mod.max_depth = int(sys.argv[3])
    if sys.argv[4] == "None":
        mod.max_depth = None
    else:
        mod.max_depth = int(sys.argv[4])
    mod.model_run("EURUSD1.csv", "Target")
