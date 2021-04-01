-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: varela_tavares_alexandre_info1b_gestion_de_facture

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS varela_tavares_alexandre_info1b_gestion_de_facture;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS varela_tavares_alexandre_info1b_gestion_de_facture;

-- Utilisation de cette base de donnée

USE varela_tavares_alexandre_info1b_gestion_de_facture;
-- --------------------------------------------------------

--
-- Structure de la table `t_attente`
--

CREATE TABLE `t_attente` (
  `id_attente` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_facture` int(11) NOT NULL,
  `date_entree_facture` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_attente`
--

INSERT INTO `t_attente` (`id_attente`, `fk_user`, `fk_facture`, `date_entree_facture`) VALUES
(1, 1, 1, '2021-03-03'),
(2, 2, 2, '2021-03-04'),
(3, 3, 3, '2021-03-16');

-- --------------------------------------------------------

--
-- Structure de la table `t_destinataire`
--

CREATE TABLE `t_destinataire` (
  `id_destinataire` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_facture` int(11) NOT NULL,
  `destinataire` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_destinataire`
--

INSERT INTO `t_destinataire` (`id_destinataire`, `fk_user`, `fk_facture`, `destinataire`) VALUES
(1, 1, 1, 'Groupe Mutuel'),
(2, 2, 2, 'Etat de vaud '),
(3, 3, 3, 'Etat de vaud ');

-- --------------------------------------------------------

--
-- Structure de la table `t_facture`
--

CREATE TABLE `t_facture` (
  `id_facture` int(11) NOT NULL,
  `numero_facture` int(11) NOT NULL,
  `somme` float NOT NULL,
  `delai` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_facture`
--

INSERT INTO `t_facture` (`id_facture`, `numero_facture`, `somme`, `delai`) VALUES
(1, 2021, 500, '2021-04-01'),
(2, 2000, 423.25, '2021-03-31'),
(3, 312, 450, '2021-03-31');

-- --------------------------------------------------------

--
-- Structure de la table `t_motif`
--

CREATE TABLE `t_motif` (
  `id_motif` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_facture` int(11) NOT NULL,
  `motif` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_motif`
--

INSERT INTO `t_motif` (`id_motif`, `fk_user`, `fk_facture`, `motif`) VALUES
(1, 1, 1, 'assurance maladie'),
(2, 2, 2, 'amende pour conduite sans permis '),
(3, 3, 3, 'Fournitures scolaires');

-- --------------------------------------------------------

--
-- Structure de la table `t_payement`
--

CREATE TABLE `t_payement` (
  `id_payement` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_facture` int(11) NOT NULL,
  `date_de_payement` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_payement`
--

INSERT INTO `t_payement` (`id_payement`, `fk_user`, `fk_facture`, `date_de_payement`) VALUES
(1, 1, 1, '2021-03-02'),
(2, 2, 2, '2021-03-04'),
(3, 3, 3, '2021-03-23');

-- --------------------------------------------------------

--
-- Structure de la table `t_rappel`
--

CREATE TABLE `t_rappel` (
  `id_rappel` int(11) NOT NULL,
  `fk_user` int(11) NOT NULL,
  `fk_facture` int(11) NOT NULL,
  `date_de_rappel` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_rappel`
--

INSERT INTO `t_rappel` (`id_rappel`, `fk_user`, `fk_facture`, `date_de_rappel`) VALUES
(1, 1, 1, '2021-03-31'),
(2, 2, 2, '2021-03-30'),
(3, 3, 3, '2021-03-24');

-- --------------------------------------------------------

--
-- Structure de la table `t_user`
--

CREATE TABLE `t_user` (
  `id_user` int(11) NOT NULL,
  `nom_user` varchar(30) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_user`
--

INSERT INTO `t_user` (`id_user`, `nom_user`, `email`, `password`) VALUES
(1, 'alex2001', 'alex2001@gmail.com', 'root'),
(2, 'marie2', 'marie2@gmail.com', 'rooter'),
(3, 'gaspar12', 'gaspardu13@hotmail.com', 'gaspargaspar'),
(4, 'marlene', 'marleche@gmail.com', 'password');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_attente`
--
ALTER TABLE `t_attente`
  ADD PRIMARY KEY (`id_attente`),
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_facture` (`fk_facture`);

--
-- Index pour la table `t_destinataire`
--
ALTER TABLE `t_destinataire`
  ADD PRIMARY KEY (`id_destinataire`),
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_destinataire` (`fk_facture`);

--
-- Index pour la table `t_facture`
--
ALTER TABLE `t_facture`
  ADD PRIMARY KEY (`id_facture`);

--
-- Index pour la table `t_motif`
--
ALTER TABLE `t_motif`
  ADD PRIMARY KEY (`id_motif`),
  ADD UNIQUE KEY `fk_motif` (`fk_facture`),
  ADD KEY `fk_user` (`fk_user`);

--
-- Index pour la table `t_payement`
--
ALTER TABLE `t_payement`
  ADD PRIMARY KEY (`id_payement`),
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_facture` (`fk_facture`),
  ADD KEY `fk_facture_2` (`fk_facture`),
  ADD KEY `fk_facture_3` (`fk_facture`),
  ADD KEY `fk_facture_4` (`fk_facture`);

--
-- Index pour la table `t_rappel`
--
ALTER TABLE `t_rappel`
  ADD PRIMARY KEY (`id_rappel`),
  ADD KEY `fk_user` (`fk_user`),
  ADD KEY `fk_facture` (`fk_facture`);

--
-- Index pour la table `t_user`
--
ALTER TABLE `t_user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_attente`
--
ALTER TABLE `t_attente`
  MODIFY `id_attente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_destinataire`
--
ALTER TABLE `t_destinataire`
  MODIFY `id_destinataire` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_facture`
--
ALTER TABLE `t_facture`
  MODIFY `id_facture` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_motif`
--
ALTER TABLE `t_motif`
  MODIFY `id_motif` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_payement`
--
ALTER TABLE `t_payement`
  MODIFY `id_payement` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_rappel`
--
ALTER TABLE `t_rappel`
  MODIFY `id_rappel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `t_user`
--
ALTER TABLE `t_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `t_attente`
--
ALTER TABLE `t_attente`
  ADD CONSTRAINT `t_attente_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_attente_ibfk_2` FOREIGN KEY (`fk_facture`) REFERENCES `t_facture` (`id_facture`);

--
-- Contraintes pour la table `t_destinataire`
--
ALTER TABLE `t_destinataire`
  ADD CONSTRAINT `t_destinataire_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_destinataire_ibfk_2` FOREIGN KEY (`fk_facture`) REFERENCES `t_facture` (`id_facture`);

--
-- Contraintes pour la table `t_motif`
--
ALTER TABLE `t_motif`
  ADD CONSTRAINT `t_motif_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_motif_ibfk_2` FOREIGN KEY (`fk_facture`) REFERENCES `t_facture` (`id_facture`);

--
-- Contraintes pour la table `t_payement`
--
ALTER TABLE `t_payement`
  ADD CONSTRAINT `t_payement_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_payement_ibfk_2` FOREIGN KEY (`fk_facture`) REFERENCES `t_facture` (`id_facture`);

--
-- Contraintes pour la table `t_rappel`
--
ALTER TABLE `t_rappel`
  ADD CONSTRAINT `t_rappel_ibfk_1` FOREIGN KEY (`fk_user`) REFERENCES `t_user` (`id_user`),
  ADD CONSTRAINT `t_rappel_ibfk_2` FOREIGN KEY (`fk_facture`) REFERENCES `t_facture` (`id_facture`);


