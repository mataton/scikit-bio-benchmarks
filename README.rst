=====================
scikit-bio-benchmarks
=====================

Performance benchmarks for the `scikit-bio <https://github.com/scikit-bio/scikit-bio>`_ library.

Overview
--------

This repository contains performance benchmarks for scikit-bio using `ASV (airspeed velocity) <https://asv.readthedocs.io/>`_. 
The benchmarks track performance across different releases to identify regressions and improvements over time.

🔗 **View Live Results**: https://scikit.bio/scikit-bio-benchmarks

Features
--------

- Benchmarking of scikit-bio releases
- Performance tracking across versions
- Interactive web interface for exploring results
- GitHub Actions integration for automated deployment

Contributing
------------

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Add your benchmarks following existing patterns
4. Test locally
5. Submit a pull request

For benchmark ideas, see the `scikit-bio documentation <https://scikit.bio/>`_
or check existing `GitHub issues <https://github.com/scikit-bio/scikit-bio/issues>`_.


Local Development
~~~~~~~~~~~~~~~~~

1. Clone the repository::

    # or clone your own fork of the repository
    git clone https://github.com/scikit-bio/scikit-bio-benchmarks.git
    cd scikit-bio-benchmarks

2. Install dependencies::

    pip install asv
    pip install scikit-bio

3. Run benchmarks::

    # Quick benchmarks for current version
    asv run --quick

    # Benchmark specific version
    asv run 0.6.3^!

4. Generate and view results::

    asv publish
    asv preview

Triggering Benchmarking
-----------------------

This repository uses GitHub Actions to automatically benchmark new scikit-bio releases:

1. **Manual Trigger**: Go to Actions → "Benchmark Specific Releases" → "Run workflow"
2. **Add New Version**: Enter the new release version (e.g., ``0.6.4``)
3. **Deploy**: Results are automatically published to GitHub Pages

The workflow will:

- Add the new version to ``versions.txt``
- Run benchmarks for the specified version
- Generate HTML reports
- Deploy to GitHub Pages
- Commit the updated version list


Configuration
-------------

Key configuration files:

- ``asv.conf.json``: ASV configuration and build settings
- ``versions.txt``: List of scikit-bio versions to benchmark
- ``.github/workflows/benchmark.yml``: Automated benchmarking workflow

Resources
---------

- `ASV Documentation <https://asv.readthedocs.io/>`_
- `scikit-bio Documentation <https://scikit.bio/>`_
- `GitHub Actions Documentation <https://docs.github.com/en/actions>`_

License
-------

scikit-bio-benchmarks is available under the new BSD license. See `LICENSE.txt <LICENSE.txt>`_ for scikit-bio-benchmarks's license.