# Awari retrograde analysis

This project provides supplementary material to this original publication:

John W. Romein, Henri E. Bal (2003):
"Solving the Game of Awari using Parallel Retrograde Analysis",
IEEE Computer, Vol. 36, No. 10

The paper describes a method to compute the full game state of the African
board game Awari.  Awari involves placing 48 seeds in 12 pits, and players
take turns fetching the seeds out of one of their 6 pits, and spreading
("sowing") them counter-clockwise over the other pits.
A player captures stones by sowing the last stone into an opponent’s pit so
that it contains either two or three stones. If the second-to-last pit is
also an opponent’s pit containing two or three stones, the player captures
these stones as well, and so on, moving clockwise until reaching the player’s
own pit or an opponent’s pit with fewer than two or more than three stones.

The paper discusses the challenge to compute the best possible move from
an arbitrary position, of which there are about 889 billion (actually
889,063,398,406 to be precise).  The computational effort is significant,
as are the memory and storage requirements, yet with special techniques,
it was possible to tackle this on a cluster of 72 compute nodes over
20 years ago.  Nowadays it is possible to compute the same data on a 
single compute node, provided it has enough memory (e.g., 1 TB).

This repository contains a small subset of the full Awari score databases
to make them available for further research, e.g., deep learning approaches
to learn playing the game automatically (though likely not perfectly)
by modern approaches like Alpha Zero.

The repository also includes sample code to retrieve the score of an
arbitrary position.  Given the number of seeds, this involves computing
the "Goedel number" of a position, which is an index in the corresponding
database file.  Every entry in the database is a value between -48 and 48,
representing the difference in number of stones the player to move can score
with optimal play.

Access to the full database will be provided shortly, using a different
platform suitable for sharing large datasets for research.
