# What it is?

Draw SIP (Session Initiation Protocol) sequence diagram with Mermaid

# Requirement

[Mermaid documentation](https://knsv.github.io/mermaid/)

```
% npm -g install mermaid --save-dev
```

[imgcat for iterm2 MacOS](https://raw.githubusercontent.com/gnachman/iTerm2/master/tests/imgcat)

```
Set script path like ~/.zshrc
```

# USAGE

```
% mermaid -w 600 testGraph.mmd
% imgcat testGraph.mmd.png
```

![](https://github.com/byung-u/SIP_sequence_diagram/mermaid_sequence_diagram.glf)
