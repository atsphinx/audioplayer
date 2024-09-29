====================
atsphinx-audioplayer
====================

Overview
========

This is Sphinx extension that renders html content for playing audio files.
You can display your audio media contents with documentation by this.

.. toctree::
   :maxdepth: 1

   changes

Installation
============

Register this as dependencies.

.. code-block:: console

   pip install atsphinx-audioplayer

And, set as extension into your ``conf.py``.

.. code-block:: python

   extensions = [
       "atsphinx.audioplayer",
   ]

Usage
=====

You can write directive or role to insert audio control.

Directive style
---------------

.. tab-set-code::

   .. code-block:: rst

      .. audio:: example.mp3

   .. code-block:: md

      ```{audio} example.mp3
      ```

.. audio:: description.mp3

.. only:: revealjs or dirrevealjs

   .. revealjs-break::

   You can set ``data-autoplay`` options when building as revealjs.

   .. tab-set-code::

      .. code-block:: rst

         .. audio:: example.mp3
            :no-controls:
            :data-autoplay:

      .. code-block:: md

         ```{audio} example.mp3
         :no-controls:
         :data-autoplay:
         ```

   .. audio:: description.mp3
      :no-controls:
      :data-autoplay:

Role style
----------

.. tab-set-code::

   .. code-block:: rst

      :audio:`example.mp3`

   .. code-block:: md

      {audio}`example.mp3`

You can insert audio element :audio:`description-for-role.mp3` in line.

Configuration for extension
===========================

Currently, this does not have configuration settings.

Defined directives
==================

.. rst:directive:: audio

   .. rst:directive:option:: no-controls
      :type: bool

      If this is set, write ``audio`` element excluded ``controls`` attribute.
      You can use for register audio element without user control interface.
