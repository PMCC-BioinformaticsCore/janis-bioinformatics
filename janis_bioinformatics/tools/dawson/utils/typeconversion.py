# function that takes the inputs of a tool and changes every bam type into the respecitve cram type
# while also keeping anything else the same
def cast_input_bams_to_crams(inputs):

    for inp in inputs:

        # we need to store it the input was optional originally
        is_optional = inp.input_type.optional

        # we need to check for BamBai first, as due to inheritance, the bambai is also a bam
        if isinstance(inp.input_type, BamBai):
            inp.input_type = CramCrai()
        elif isinstance(inp.input_type, Bam):
            inp.input_type = Cram()
        elif isinstance(inp.input_type, Array) and isinstance(
            inp.input_type.subtype(), BamBai
        ):
            inp.input_type = Array(CramCrai)
        elif isinstance(inp.input_type, Array) and isinstance(
            inp.input_type.subtype(), Bam
        ):
            inp.input_type = Array(Cram)
        elif inp.id() == "intervals":
            inp.input_type = String()

        # and now that we changed things, we set the optional state again
        inp.input_type.optional = is_optional

    return inputs
