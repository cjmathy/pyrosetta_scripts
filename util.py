__author__ = "Christopher Mathy"
__email__ = chris.mathy@ucsf.edu

import pandas as pd


def make_residue_scores_table(pose):
    """
    Function to create a pandas dataframe containing
    score information for each residue.
    
    Input arguments:
    pose = a pyrosetta.rosetta.core.pose object
    
    Returns:
    df - a Pandas dataframe
    """

    terms_dict = pyrosetta.rosetta.core.scoring.ScoreType.__members__
    df = pd.DataFrame(index = range(1, pose.total_residue()),
                      columns = pose.scores.keys())

    for res in (range(1, pose.total_residue())):
        df.loc[res, 'position'] = pose.pdb_info().number(res)
        df.loc[res, 'aa'] = pose.residue(res).name()
        for score in pose.scores:
            term = terms_dict[score]
            df.loc[res, score] = pose.energies().residue_total_energies(res)[term]

    cols = list(df.columns)
    cols_reordered = cols[-2:] + cols[:-2]
    df = df[cols_reorded]

    df.position.astype(int)
    
    return df
