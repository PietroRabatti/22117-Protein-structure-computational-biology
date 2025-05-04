# Displaying the Binding pocket
# Replace 'example' with the specific protein of interest
bg White, 
set cartoon_fancy_helices, 1,
set cartoon_dumbbell_length, 0.9
remove solvent
set valence, 0
cmd.set("cartoon_color", "palegreen", 'example', quiet=0)

# View residues within a specified distance (e.g., 4 Å)
extract LIG, resn LIG
util.cba(124,"LIG",_self=cmd)
select pocket, (br. all within 4 of resn LIG)
cmd.show("sticks"    ,"pocket")

# Show polar contancs
cmd.hide("cartoon"   ,"model_0")
cmd.dist("LIG_polar_conts","(LIG)","(not LIG)",quiet=1,mode=2,label=0,reset=1);cmd.enable("LIG_polar_conts")

set_view (\
     0.672511816,   -0.701226354,   -0.236653253,\
     0.513222456,    0.211492717,    0.831785738,\
    -0.533223808,   -0.680843174,    0.502119303,\
     0.000000000,    0.000000000, -239.632263184,\
     5.719275475,   20.380325317,   31.266162872,\
  -3289.246093750, 3768.510742188,  -20.000000000 )

# Choose fileName
ray 1600, 1600
png fileName, dpi=300
