# scikit-bio-benchmarks

Performance benchmarks for the `scikit-bio <https://github.com/scikit-bio/scikit-bio>`_ library.

Overview
--------

This repository contains performance benchmarks for scikit-bio using `ASV (airspeed velocity) <https://asv.readthedocs.io/>`_. 
The benchmarks track performance across different releases to identify regressions and improvements over time.

🔗 **View Live Results**: https://scikit.bio/scikit-bio-benchmarks

Features
--------

- Automated benchmarking of scikit-bio releases
- Performance tracking across versions
- Interactive web interface for exploring results
- GitHub Actions integration for automated deployment

Repository Structure
--------------------

::

    scikit-bio-benchmarks/
    ├── benchmarks/          # Benchmark definitions
    ├── .github/workflows/   # GitHub Actions workflows
    ├── asv.conf.json       # ASV configuration
    ├── versions.txt        # List of versions to benchmark
    └── README.rst          # This file

Quick Start
-----------

Local Development
~~~~~~~~~~~~~~~~~

1. Clone the repository::

    git clone https://github.com/yourusername/scikit-bio-benchmarks.git
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

Adding New Benchmarks
~~~~~~~~~~~~~~~~~~~~~

1. Create benchmark functions in the ``benchmarks/`` directory
2. Follow ASV naming conventions (functions starting with ``time_`` or ``mem_``)
3. Test locally with ``asv run --quick``
4. Submit a pull request

Automated Benchmarking
----------------------

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