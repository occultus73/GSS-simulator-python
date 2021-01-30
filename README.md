# GSS-simulator-python
Demo video here: https://youtu.be/Ii-yRrk7r98

Regard the <b>output</b> directory for all of the graphed simulation results. Each generational directory contains 60,096 matplotlib graphs.

## Explantion
This "GSS Simulator" is actually comprised of three different simulations: 
  1) Actual Fertility, 
  2) Ideal Fertility, 
  3) Sterile Fertility.
  
All three of these simulations extract their samples from the 1994-2018 GSS datasets, where all metrics that each simulation requires for each given survee are available. All graphs that are provided within the output directory purport to represent the US adult working population (18-67). None of the simulations will plot data that is based on less than a hundred individuals (actual or generated), and therefore simulations will sometime start late or terminate early, or dissapear completely; indeed, for some extremely-filtered analyses, the graphs are completely blank for this reason, unfortunately.

For further details, the reader is encouraged to review the improvisational discussion of this Simulator in the video linked above.

### Definitions
<b>Actual Fertility:</b> "Actual" fertility here refers to fertility that is based on completed fertility data in the GSS, where the GSS defines the age of completed fertility for women as being 41 and men as being 45.

<b>Ideal Fertility:</b> "Ideal" fertility here refers to the number of children that a GSS survee reports as being "ideal."

<b>Sterile Fertility:</b> An oxymoronic term employed in referring to the hypothetical scenario in which nobody in the GSS sample has any children at all and everyone is left to retire and die of old age, unto extinction. The sterile simulation is to some extent an emperical report of what is actually occuring in the real US population over time, especially after controlling for age-related effects.

<b>Asexual Fertility:</b> The simulations model on the basis of asexual reproduction - all children are born of one parent. The reported actual or ideal number of children by each GSS survee is therefore halved (and rounded probibalisticly upon each evaluation).

<b>Heritable Fertility:</b> In the fertility simulations, children inherit, not only the exact same social attiudes as their parent, but their fertility as well; that is, their age at which they start having children and the number of children they have.

<b>Fertility Simulations:</b> The "Actual Fertility" and "Ideal Fertility" are the two "fertility simulations." They are predicated on hertiable and asexual reproduction as clarified above. "Fertility simulations" is not used to refer the "Sterile Fertility" simulation, which is by definition not fertile at all, and thereby not heritable or asexual in any meaningful sense either.

### Statement of Limitations
1. The fertility simulations operate on the basis of absolute heritability. The sterile simulation itself, together with common sense, attests to the degree to which reported social attitudes in the US have been driven by the evolving sociopolitical, economic, technological and cultural environment, rather than differential reproduction of various heritabile personality traits. The fertility simulations therefore cannot be taken as prophetic or predictive, in any naive, direct sense (for one thing, they always culminate in impossible over-population scenarios). However, this author would posit that differential reproduction of partially-heritabile personality traits, does indeed have a substantial long term effect on populations, and this evolutionary force is likely a significant contributor to the "Gen-Z" reversal effects that the Sterile simulation reveals in many graphs towards the end of the epoch. It should also be stated that, regarding IQ, the fertility simulations are somewhat effective as direct predictors of the future, inasmuch as they parallel the Sterile simulation, which is consistent with the literature that demonstrates adult IQ to be >80% heritiable.

2. The fertility simulations have a few sampling biases. The largest one being that the actual fertility excludes all adults under 40, because it requires completed fertility. A less significant sampling bias is caused by the fertility simulations requiring the "age at first child" metric - there are many parents in the GSS surveys for which this metric is unavailable, and they are skipped over - for those that report never having, or idealize as never having, children, this requirement is waived, and thus more actual/ideologically childfree individuals are loaded in. For the Ideal Simulation specfically, some individuals in the GSS surveys report idealizing as having more than one child, but for which their "age at first child" metric is unknown, possibly because they were yet to have their first child - however, preliminary analysis showed the number of such cases to be surprisingly insignificant, which testifies to the insignificance of the bias produced by requiring "age at first child" more generally.

3. Finally, although it is not an actual limitation, because it represents a genuine phenomenon in reality, women have a disproportionately larger effect on the fertility simulations because they have children at a younger age than men (also inasmuch as there is a small childfree sample bias, childfree individuals are more likely to be male, insofar as more reproductive inequality exists among males). The evolutionary implications of the fact that one sex has more influence over the genepool than the other when there is a substantial difference at which age reproduction begins, is an important finding of this Simulator and worthy of seperate discussion by itself. There is literature showing that paternal age predicts a given societies' birth sex ratio.
