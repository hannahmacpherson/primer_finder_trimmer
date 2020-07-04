



#function to remove first line and make sequence one string
def tidy(sequence_file):
    lines = sequence_file.readlines()
    remove_first_line = lines[1:]
    remove_new_lines = [ item[0:-2] for item in remove_first_line]
    tidied_sequence = ''.join(remove_new_lines)
    return tidied_sequence



# function to find the forward primer and trim x basepairs upstream then the reverse and trim y basepairs downstream
# three different options for primers since HLA is v polymorphic and the likelihood of every sequence matching one primer is relatively low
def trim(tidied_sequence, number_of_extra_bps_upstream, number_of_extra_bps_downstream, sequence_name, forward_primer_option1, forward_primer_option2, forward_primer_option3, reverse_primer_complement_option1, reverse_primer_complement_option2, reverse_primer_complement_option3):
    start_position = tidied_sequence.find(forward_primer_option1)
    if start_position == -1:
        start_position = tidied_sequence.find(forward_primer_option2)
        if start_position == -1:
            start_position = tidied_sequence.find(forward_primer_option3)
    end_position = (tidied_sequence.find(reverse_primer_complement_option1)) 
    if end_position == -1:
        end_position = (tidied_sequence.find(reverse_primer_complement_option2)) + len(reverse_primer_complement_option2)
    else: end_position = (tidied_sequence.find(reverse_primer_complement_option1)) + len(reverse_primer_complement_option1)
    end_position += len(reverse_primer_complement_option1)
    if len(tidied_sequence[end_position:]) >= number_of_extra_bps_downstream:
        trim_off_end_part = tidied_sequence[:(end_position + number_of_extra_bps_downstream)]
    else: 
        trim_off_end_part = tidied_sequence
    if len(tidied_sequence[:start_position]) >= number_of_extra_bps_upstream:
        trimmed_sequence = trim_off_end_part[(start_position - number_of_extra_bps_upstream):]
    else: 
        trimmed_sequence = trim_off_end_part
    trimmed_sequence_length = len(trimmed_sequence)
    if trimmed_sequence_length == 0:
        print(f"Trimming failed for {sequence_name}, sequence likely doesn't contain a version of the forward and/or reverse primer.")
    return trimmed_sequence


# function to save new file with descriptive header ready for MAFFT
def save(folder, trimmed_sequence, sequence_name):
    file_name = sequence_name + "_trimmed.txt"
    top_line = f">{sequence_name}_trimmed\n"

    with open(f"{folder}/{file_name}", 'w') as new_file: # saves it within the same folder as the input local sequence files
        new_file.writelines([top_line, trimmed_sequence])



# function to combine tidy, trim and save to a given .txt file
def tidy_trim_save(folder, sequence_txt_file, number_of_extra_bps_upstream, number_of_extra_bps_downstream, forward_primer_option1, forward_primer_option2, forward_primer_option3, reverse_primer_complement_option1, reverse_primer_complement_option2, reverse_primer_complement_option3): 

    with open(f"{folder}/{sequence_txt_file}") as sequence_file:

        sequence_name = sequence_txt_file[:-4] # aka removing .txt from the end

        # using functions
        tidied_sequence = tidy(sequence_file)

        trimmed_sequence = trim(tidied_sequence, number_of_extra_bps_upstream, number_of_extra_bps_downstream, sequence_name, forward_primer_option1, forward_primer_option2, forward_primer_option3, reverse_primer_complement_option1, reverse_primer_complement_option2, reverse_primer_complement_option3)

        save(folder, trimmed_sequence, sequence_name)
        
        print(f"{sequence_name}.txt exported.")