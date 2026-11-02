#!/usr/bin/env python3
"""Plot committed direct comparisons; errors are descriptive standard errors."""
import json
import os
import sys
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR','/tmp/patterson-matplotlib')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/patterson-font-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    here=Path(__file__).resolve().parent
    old=json.loads((here/'results/direct_1e6.extended.json').read_text())
    new=json.loads((here/'results/direct_1e7.extended.json').read_text())
    plt.rcParams.update({'svg.hashsalt':'patterson-direct-2026','svg.fonttype':'none',
                         'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig=plt.figure(figsize=(10,8),layout='constrained')
    gs=fig.add_gridspec(2,2,height_ratios=[1,1.1])
    for col,res in enumerate([1,7]):
        ax=fig.add_subplot(gs[0,col])
        candidate=[r for r in new['rows'] if r['range']=='pooled' and r['residue']==res]
        ax.plot([r['u'] for r in candidate],[r['predicted'] for r in candidate],color='#222222',lw=1.2,label='Candidate grid values')
        for data,label,color,marker in [(old,'Through 1 million','#b65e18','s'),(new,'Through 10 million','#1674aa','o')]:
            rows=[r for r in data['rows'] if r['range']=='pooled' and r['residue']==res]
            ax.errorbar([r['u'] for r in rows],[r['mean'] for r in rows],
                        yerr=[r['stderr'] for r in rows],fmt=marker,ms=3,
                        color=color,alpha=.85,lw=.7,capsize=1.5,label=label)
        ax.set(title=f'Primes congruent to {res} modulo 12',xlabel='u = k/24',ylabel='Mean of S_p(floor(up)) / p^(5/6)')
        ax.grid(alpha=.15)
        if col==0: ax.legend(fontsize=8,loc='best')
    ax=fig.add_subplot(gs[1,:])
    for res,color in [(1,'#1674aa'),(7,'#b65e18')]:
        rows=[r for r in new['diagnostics'] if r['range']=='dyadic' and r['residue']==res]
        ax.plot(range(len(rows)),[r['descriptive_amplitude_ratio'] for r in rows],'-o',color=color,ms=4,label=f'Class {res}')
    labels=[f'2^{r["lo"].bit_length()-1}–2^{r["lo"].bit_length()}' for r in rows]
    labels[-1]='2^23–10 million'
    ax.set_xticks(range(len(rows)),labels,rotation=20)
    ax.axhline(1,color='#222222',lw=1,ls='--')
    ax.set(title='Dyadic amplitude ratios: offsets change sign',ylabel='Projection onto candidate profile',xlabel='Prime range (last interval is partial)')
    ax.legend(); ax.grid(alpha=.15)
    fig.suptitle('Exact direct sums: pooled agreement improves; dyadic drift is not monotone',fontsize=13)
    fig.supxlabel('All comparisons use p >= 65,536. Error bars: one descriptive standard error.\nGrid values are correlated; no calibrated confidence or significance claim.',fontsize=9)
    fig.savefig(here/'results/direct_profiles.svg',metadata={'Date':None})
    if len(sys.argv)>1:
        fig.savefig(sys.argv[1],dpi=140)
    plt.close(fig)


if __name__=='__main__': main()
