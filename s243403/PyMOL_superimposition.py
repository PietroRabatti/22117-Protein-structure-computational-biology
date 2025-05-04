fetch 5egg
fetch 2cyx
split_chains
select chainBC, chain B+C
remove chainBC
super 5egg_A, 2cyx_A
remove solvent
color gray90, 5egg_A
color gray90, 2cyx_A

select Loop1_5egg, 5egg_A and resi 69-86
select Loop1_2cyx, 2cyx_A and resi 73-90
color palegreen, Loop1_2cyx or Loop1_5egg

select Loop2_5egg, 5egg_A and resi 112-119
select Loop2_2cyx, 2cyx_A and resi 130-134
color palegreen, Loop2_2cyx or Loop2_5egg

select Loop3_5egg, 5egg_A and resi 91-98
select Loop3_2cyx, 2cyx_A and resi 95-114
color palegreen, Loop3_2cyx or Loop3_5egg

set_view (\
     0.260281026,   -0.772344351,   -0.579428494,\
     0.871456087,   -0.070466518,    0.485386789,\
    -0.415715516,   -0.631282806,    0.654722035,\
     0.000000000,    0.000000000, -189.409835815,\
     6.222787857,   19.831562042,   31.727588654,\
   133.150558472,  245.669158936,  -20.000000000 )

bg White
set fog, 2
ray 1400, 1400
png Super, dpi=300
