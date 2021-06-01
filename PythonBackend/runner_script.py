import sys
import os
import modelc
import modeld

# @mo2a comment 2l path da w 7ot 2l path bta3k gmbo w delete this comment
filePATH = '../Dataset/' + str(sys.argv[2])
csvPATH = '../Dataset/' + str(sys.argv[2]) + '/dataset.csv'
outputPATH = '../Dataset/' + str(sys.argv   [2]) + '/result.png'

if int(sys.argv[1]) == 0:
    model_type = sys.argv[1]
    mod_layer_count = sys.argv[3]
    mod_layer_data_string = sys.argv[4]

    # Convert args string to array
    mod_data_list = mod_layer_data_string.split("],")
    d = [i.strip('[') for i in mod_data_list]
    d = [i.strip(']') for i in d]

    final_data_list = []
    for i in range(len(d)):
        final_data_list.append(list(d[i].split(",")))
    epochs = sys.argv[5]
    '''
    model_type = 0
    mod_layer_count = 3
    final_data_list = [[12,8,'relu'],[8,4,'sigmoid'],[4,2,'sigmoid']]
    epochs = 10
    '''
    try:
        mod = modelc.model_class(
            model_type, mod_layer_count, final_data_list, epochs)

        mod.model_run(filePATH)
    except Exception as e:
        print(e)

    #target_model = modelc.model()
elif int(sys.argv[1]) == 1:
    mod = modeld.modeld_class()

    mod.max_depth = int(sys.argv[3])
    mod.max_depth = int(sys.argv[4])
    mod.max_depth = int(sys.argv[5])

    mod.model_run(filePATH)
