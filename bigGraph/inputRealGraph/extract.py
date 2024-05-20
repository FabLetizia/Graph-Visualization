input_file = 'DBLP.txt'
output_graph_file = 'out.graph'
output_txt_file = 'description.txt'

def process_file(input_file, output_graph_file, output_txt_file):
    edges_dict = {}

    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split()
            edge = tuple(sorted(parts[:2]))
            remaining_parts = parts[2:]
            filtered_parts = [part for index, part in enumerate(remaining_parts) if index % 2 != 0]

            if edge in edges_dict:
                edges_dict[edge].extend(filtered_parts)
            else:
                edges_dict[edge] = filtered_parts

    with open(output_graph_file, 'w') as graph_file, \
         open(output_txt_file, 'w') as txt_file:
        
        for edge, values in edges_dict.items():
            graph_file.write(f"{int(edge[0]) + 1}\t{int(edge[1]) + 1}\n")
            txt_file.write(f"{int(edge[0]) + 1}\t{int(edge[1]) + 1}\t" + "\t".join(values) + '\n')

process_file(input_file, output_graph_file, output_txt_file)
