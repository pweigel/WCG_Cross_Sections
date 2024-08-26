import numpy as np
from matplotlib import pyplot as plt
import photospline

# Select a range of log10 energy in GeV
log10_energies = np.linspace(np.log10(50), np.log10(5e12), 101)

# Create spline table w/ photospline
projectile = 'neutrino'
target = 'isoscalar'
flavor = 'total'
spline_fn = f'../CT18ANNLO/sigma_splines/sigma_CT18ANNLO_nf6_sx_{projectile}_{target}_{flavor}.fits'
spline = photospline.SplineTable(spline_fn)

# Evaluate the spline at log10(E), get log10(xs)
log10_xs = spline.evaluate_simple([log10_energies])

# Load xs table for comparison
table_fn = '../CT18ANNLO/CT18ANNLO_isoscalar.table'
table_energies = np.zeros(36)
table_xs = np.zeros(36)
with open(table_fn) as f:
    for i, line in enumerate(f.readlines()):
        values = [float(x) for x in line.rstrip('\n').split(',')]
        table_energies[i] = values[0]
        table_xs[i] = values[1]

# Plot the cross section from the spline and the table
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(10**log10_energies, 10**log10_xs)
ax.scatter(table_energies, table_xs, color='k')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([5e1, 5e12])

ax.set_xlabel('energy [GeV]')
ax.set_ylabel('sigma [pb]')

plt.savefig('cross_section.png')