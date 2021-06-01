import sys
import modelc
import modeld

filePATH = '../Dataset/' + str(sys.argv[2])

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

    try:
        mod = modelc.model_class(
            model_type, mod_layer_count, final_data_list, epochs)

        mod.model_run(filePATH)
    except Exception as e:
        print(e)

elif int(sys.argv[1]) == 1:
    mod = modeld.modeld_class()

    mod.max_depth = int(sys.argv[3])
    mod.max_depth = int(sys.argv[4])
    mod.max_depth = int(sys.argv[5])

    mod.model_run(filePATH)
